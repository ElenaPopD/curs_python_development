from django.core.management.base import BaseCommand, CommandError  # noqa: F401
from app.models import Produs  # noqa: F401

class Command(BaseCommand):
    def add_arguments(self, parser):
            parser.add_argument("stoc", type=int, help="Seteaza stocul la valoarea specificata")
            parser.add_argument("--test", type = bool, default = False, help="Testeaza comanda")
            return super().add_arguments(parser)

    def handle(self, *args, **options):
        print("in comand")
        from pprint import pprint
        pprint(args)
        pprint(options)
        print("in comand")
        modified = Produs.objects.all().update(stoc=options["stoc"])
        print(f"AM modificat {modified} produse!")