from django.core.management.base import BaseCommand
from django.db.models import Q
from game.models import GameWord

class Command(BaseCommand):
    help = 'Remove 4-letter words from the database'

    def handle(self, *args, **options):
        # Find all 4-letter words using extra() or by checking length in Python
        all_words = GameWord.objects.all()
        four_letter_words = []
        
        for word in all_words:
            if len(word.word) == 4:
                four_letter_words.append(word)
        
        count = len(four_letter_words)
        
        if count > 0:
            self.stdout.write(f'Found {count} 4-letter words to remove:')
            for word in four_letter_words:
                self.stdout.write(f'  - {word.word}')
            
            # Delete them
            for word in four_letter_words:
                word.delete()
            
            self.stdout.write(
                self.style.SUCCESS(f'Successfully removed {count} 4-letter words from database.')
            )
        else:
            self.stdout.write(
                self.style.SUCCESS('No 4-letter words found in database.')
            )
        
        # Show remaining word count
        total_words = GameWord.objects.count()
        self.stdout.write(f'Total words remaining: {total_words}')
