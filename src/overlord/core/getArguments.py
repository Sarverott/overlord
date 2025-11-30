from argparse import ArgumentParser


def argExecutor(self):
    self.options = ArgumentParser(
        prog=self.name, description=self.description, epilog=self.randomSentences.pick
    )
