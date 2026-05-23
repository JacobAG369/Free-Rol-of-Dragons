erDiagram
    auth_user {
        int id PK
        string username
        string email
        string password
    }

    %% BLOQUE SRD (Inmutable)
    srd_razas {
        int id PK
        string nombre
        jsonb incremento_atributos "Estructurado para automatización"
        int velocidad
        jsonb idiomas
        jsonb rasgos_raciales
    }

    srd_clases {
        int id PK
        string nombre
        string dado_golpe
        text descripcion
    }

    srd_conjuros {
        int id PK
        string nombre
        int nivel
        string escuela
        boolean concentracion
        text descripcion
    }

    srd_monstruos {
        int id PK
        string nombre
        int clase_armadura
        int puntos_golpe
        int fuerza
        int destreza
        int constitucion
        int inteligencia
        int sabiduria
        int carisma
        string desafio
        jsonb acciones "Estructurado para automatización"
        jsonb acciones_legendarias
    }

    srd_objetos {
        int id PK
        string nombre
        string categoria
        string rareza
        boolean es_magico
    }

    %% BLOQUE HOMEBREW (Mutable, dependiente de auth_user)
    homebrew_hechizos {
        int id PK
        string nombre
        int nivel
        string escuela
        boolean concentracion
        int creador_id FK "Ref: auth_user"
    }

    homebrew_objetos {
        int id PK
        string nombre
        string categoria
        boolean es_magico
        int creador_id FK "Ref: auth_user"
    }

    homebrew_monstruos {
        int id PK
        string nombre
        int clase_armadura
        jsonb acciones
        int creador_id FK "Ref: auth_user"
    }

    %% BLOQUE CAMPAÑA Y PERSONAJE
    user_campanas {
        int id PK
        string nombre
        int director_id FK "Ref: auth_user"
        text notas_generales
        timestamp fecha_creacion
    }

    user_personajes {
        int id PK
        int usuario_id FK "Ref: auth_user"
        int campana_id FK "Ref: user_campanas (Nullable)"
        string nombre
        int experiencia
        int raza_id FK "Ref: srd_razas"
        int fuerza
        int destreza
        int constitucion
        int inteligencia
        int sabiduria
        int carisma
        int puntos_golpe_max
        int puntos_golpe_actuales
        int clase_armadura
    }

    %% TABLAS INTERMEDIAS (Resolución de N a N)
    personaje_clases {
        int personaje_id FK
        int clase_id FK
        int nivel_en_clase
    }

    personaje_inventario {
        int personaje_id FK
        int objeto_srd_id FK "Nullable"
        int objeto_hb_id FK "Nullable"
        int cantidad
        boolean equipado
    }

    personaje_conjuros {
        int personaje_id FK
        int conjuro_srd_id FK "Nullable"
        int conjuro_hb_id FK "Nullable"
        boolean preparado
    }

    %% RELACIONES
    auth_user ||--o{ user_campanas : "dirige"
    auth_user ||--o{ user_personajes : "posee"
    auth_user ||--o{ homebrew_hechizos : "crea"
    auth_user ||--o{ homebrew_objetos : "crea"
    auth_user ||--o{ homebrew_monstruos : "crea"

    user_campanas ||--o{ user_personajes : "incluye"
    
    %% Relaciones de Construcción de Personaje
    srd_razas ||--o{ user_personajes : "define raza"
    user_personajes ||--o{ personaje_clases : "progresa en"
    srd_clases ||--o{ personaje_clases : "otorga"

    %% Relaciones de Inventario (Dual)
    user_personajes ||--o{ personaje_inventario : "tiene"
    srd_objetos ||--o{ personaje_inventario : "asigna (oficial)"
    homebrew_objetos ||--o{ personaje_inventario : "asigna (custom)"

    %% Relaciones de Conjuros (Dual)
    user_personajes ||--o{ personaje_conjuros : "conoce"
    srd_conjuros ||--o{ personaje_conjuros : "asigna (oficial)"
    homebrew_hechizos ||--o{ personaje_conjuros : "asigna (custom)"