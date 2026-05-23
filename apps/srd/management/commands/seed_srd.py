import requests
from django.core.management.base import BaseCommand

from apps.srd.models import Clase, Conjuro, Monstruo, Objeto, Raza

BASE_URL = 'https://api.open5e.com/v1'


def _extract_walk_speed(speed):
    if isinstance(speed, dict):
        return speed.get('walk', 0)
    return int(speed) if speed else 0


def _fetch_all(url):
    while url:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()
        yield from data['results']
        url = data['next']


class Command(BaseCommand):
    help = 'Pobla las tablas SRD desde la API pública Open5e'

    def handle(self, *args, **options):
        try:
            self._seed_razas()
            self._seed_clases()
            self._seed_conjuros()
            self._seed_monstruos()
            self._seed_objetos()
            self.stdout.write(self.style.SUCCESS('Seed SRD completado.'))
        except requests.RequestException as exc:
            self.stderr.write(self.style.ERROR(f'Error de red: {exc}'))

    def _seed_razas(self):
        count = 0
        for r in _fetch_all(f'{BASE_URL}/races/?limit=100'):
            Raza.objects.update_or_create(
                nombre=r['name'],
                defaults={
                    'incremento_atributos': r.get('asi', []),
                    'velocidad': _extract_walk_speed(r.get('speed', 0)),
                    'idiomas': {'texto': r.get('languages', '')},
                    'rasgos_raciales': {'texto': r.get('traits', '')},
                },
            )
            count += 1
        self.stdout.write(self.style.SUCCESS(f'  Razas: {count} registros'))

    def _seed_clases(self):
        count = 0
        for r in _fetch_all(f'{BASE_URL}/classes/?limit=100'):
            Clase.objects.update_or_create(
                nombre=r['name'],
                defaults={
                    'dado_golpe': r.get('hit_dice', ''),
                    'descripcion': r.get('desc', ''),
                },
            )
            count += 1
        self.stdout.write(self.style.SUCCESS(f'  Clases: {count} registros'))

    def _seed_conjuros(self):
        count = 0
        for r in _fetch_all(f'{BASE_URL}/spells/?limit=100'):
            concentracion = str(r.get('concentration', 'no')).lower() == 'yes'
            Conjuro.objects.update_or_create(
                nombre=r['name'],
                defaults={
                    'nivel': r.get('level_int', 0),
                    'escuela': r.get('school', ''),
                    'concentracion': concentracion,
                    'descripcion': r.get('desc', ''),
                },
            )
            count += 1
        self.stdout.write(self.style.SUCCESS(f'  Conjuros: {count} registros'))

    def _seed_monstruos(self):
        count = 0
        for r in _fetch_all(f'{BASE_URL}/monsters/?limit=100'):
            Monstruo.objects.update_or_create(
                nombre=r['name'],
                defaults={
                    'clase_armadura': int(r.get('armor_class', 0)),
                    'puntos_golpe': r.get('hit_points', 0),
                    'fuerza': r.get('strength', 0),
                    'destreza': r.get('dexterity', 0),
                    'constitucion': r.get('constitution', 0),
                    'inteligencia': r.get('intelligence', 0),
                    'sabiduria': r.get('wisdom', 0),
                    'carisma': r.get('charisma', 0),
                    'desafio': str(r.get('challenge_rating', '0')),
                    'acciones': r.get('actions') or [],
                    'acciones_legendarias': r.get('legendary_actions') or [],
                },
            )
            count += 1
        self.stdout.write(self.style.SUCCESS(f'  Monstruos: {count} registros'))

    def _seed_objetos(self):
        count = 0
        for r in _fetch_all(f'{BASE_URL}/magicitems/?limit=100'):
            Objeto.objects.update_or_create(
                nombre=r['name'],
                defaults={
                    'categoria': r.get('type', ''),
                    'rareza': r.get('rarity', ''),
                    'es_magico': True,
                },
            )
            count += 1
        for r in _fetch_all(f'{BASE_URL}/weapons/?limit=100'):
            Objeto.objects.update_or_create(
                nombre=r['name'],
                defaults={
                    'categoria': r.get('category', ''),
                    'rareza': 'estandar',
                    'es_magico': False,
                },
            )
            count += 1
        self.stdout.write(self.style.SUCCESS(f'  Objetos: {count} registros'))
