from mrjob.job import MRJob
from mrjob.step import MRStep
import re

class WordCounter(MRJob) :

    def steps(self):
        return [
            MRStep (
                mapper_raw=self.mapper_raw, 
                combiner=self.combiner, 
                reducer=self.reducer
            )
        ]
    
    def mapper_raw (self , path, uri):
        # with open(path) as f:
            print(path, uri)

if __name__ == '__main__':
    runner = WordCounter() 
    runner.run()