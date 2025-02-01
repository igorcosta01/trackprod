from django.core.management.base import BaseCommand
from estoque.models import Drive

# Definição dos drives
DRIVES = {
    # Produtos Acabados
    "A": (195, "acabado"), "B": (212, "acabado"), "C": (205, "acabado"),
    "D": (213, "acabado"), "E": (212, "acabado"), "F": (243, "acabado"),
    "G": (249, "acabado"), "H": (259, "acabado"), "P": (160, "acabado"),
    "Q": (157, "acabado"), "R": (144, "acabado"), "S": (142, "acabado"),
    "T": (142, "acabado"), "U": (142, "acabado"), "V": (141, "acabado"),
    "W": (150, "acabado"), "X": (39, "acabado"),

    # Produtos Intermediários
    "I": (140, "intermediario"), "J": (147, "intermediario"), "K": (154, "intermediario"),
    "L": (143, "intermediario"), "M": (150, "intermediario"), "N": (143, "intermediario"),
    "O": (145, "intermediario"),
}

class Command(BaseCommand):
    help = "Popula a tabela Drive com os endereços de estoque (acabado e intermediário)"

    def handle(self, *args, **kwargs):
        novos_drives = []
        for rua, (capacidade, tipo) in DRIVES.items():
            for numero in range(1, capacidade + 1):
                # Se o endereço já existir, pula a inserção
                if not Drive.objects.filter(rua=rua, numero=numero).exists():
                    novos_drives.append(Drive(rua=rua, numero=numero, ocupado=False, produto=None, tipo=tipo))

        if novos_drives:
            Drive.objects.bulk_create(novos_drives)
            self.stdout.write(self.style.SUCCESS(f"{len(novos_drives)} novos drives inseridos!"))
        else:
            self.stdout.write(self.style.WARNING("Nenhum novo drive inserido. Já está tudo no banco."))
