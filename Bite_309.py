from __future__ import annotations

import string
import os
import random
import re

EOL_PUNCTUATION = ".!?"


class Document:
    def __init__(self, filename:str) -> None:
        #filename takes a full path; not just the file name
        self.lines = []
        self.filename = filename

        if not os.path.exists(self.filename):
            with open(self.filename, 'w'): pass

        with open(self.filename, 'w+') as f:
            reader = f.readlines()
            for line in reader:
                self.lines.append(line)
            f.truncate(0)
            

    def add_line(self, line: str, index: int = None) -> Document:
        """Add a new line to the document.

        Args:
            line (str): The line,
                expected to end with some kind of punctuation.
            index (int, optional): The place where to add the line into the document.
                If None, the line is added at the end. Defaults to None.

        Returns:
            Document: The changed document with the new line.
        """
        if line[-1] not in EOL_PUNCTUATION:
            idx = random.choice([0,1,2])
            line += EOL_PUNCTUATION[idx]

        if index is None or index > len(self.lines):
            self.lines.append(line)
        else:
            self.lines.insert(index, line)
        
        with open(self.filename, 'w') as f:
            for line in self.lines:
                if line not in self.filename:
                    f.write(line + ' ' + '\n')
        
        return self



    def swap_lines(self, index_one: int, index_two: int) -> Document:
        """Swap two lines.

        Args:
            index_one (int): The first line.
            index_two (int): The second line.

        Returns:
            Document: The changed document with the swapped lines.
        """
        line1 = self.lines[index_one]
        line2 = self.lines[index_two]

        self.lines[index_one] = line2
        self.lines[index_two] = line1
        
        with open(self.filename, 'w') as f:
            for line in self.lines:
                f.write(line + ' ' + '\n')
        
        return self

    def merge_lines(self, indices: list) -> Document:
        """Merge several lines into a single line.

        If indices are not in a row, the merged line is added at the first index.

        Args:
            indices (list): The lines to be merged.

        Returns:
            Document: The changed document with the merged lines.
        """
        
        


    def add_punctuation(self, punctuation: str, index: int) -> Document:
        """Add punctuation to the end of a sentence.

        Overwrites existing punctuation.

        Args:
            punctuation (str): The punctuation. One of EOL_PUNCTUATION.
            index (int): The line to change.

        Returns:
            Document: The document with the changed line.
        """
        if punctuation not in EOL_PUNCTUATION:
            raise ValueError ('Cannot use that punctuation.')
        
        line = self.lines[index]
        line = self._remove_puctuation(line)
        line += punctuation
        self.lines[0] = line

        return self



    def word_count(self) -> int:
        """Return the total number of words in the document."""
        return len(self.words)

    @property
    def words(self) -> list:
        """Return a list of unique words, sorted and case insensitive."""
        unique_items = re.findall(r'[\w\']+', ' '.join(self.lines), re.IGNORECASE)
        return sorted(list(set(unique_items)))


    def _remove_puctuation(self, line: str) -> str:
        """Remove punctuation from a line."""
        # you can use this function as helper method for
        # Document.word_count() and Document.words
        # or you can totally ignore it
        if line[-1] in EOL_PUNCTUATION:
            punctuation = line[-1]
            line = line.replace(punctuation, '')
        else:
            pass

        return line

    def __len__(self):
        """Return the length of the document (i.e. line count)."""
        return len(self.lines)

    def __str__(self):
        """Return the content of the document as string."""
        return ' '.join([line for line in self.lines])


# if __name__ == "__main__":
#     # this part is only execute when you run the file and is ignored by the tests
#     # you can use this section for debugging and testing
#     d = (
#         Document()
#         .add_line("My first sentence.")
#         .add_line("My second sentence.")
#         .add_line("Introduction", 0)
#         .merge_lines([1, 2])
#     )

#     print(d)
#     print(len(d))
#     print(d.word_count())
#     print(d.words)


d = Document('C:/Users/superuser/Bites/bite_text.txt')
d.add_line('It is kind of chilly here today.')
print(d.lines)
d.add_line('One day it will be sunny again',0)
print(d.lines)
d.add_line('I am not happy that the dog is barking', 1)
print(d.lines)
d.add_line('You need to go home now', 3)
print(d.lines)
d.add_line('I can\'t belive she is still barking', 8)
print(d.lines)
d.add_line('xyz').swap_lines(2,4)
print(d.lines)
print(d.words)
print(d.word_count())
d.add_punctuation('!', 0)
print(d.lines)