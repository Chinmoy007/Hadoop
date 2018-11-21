from mrjob.job import MRJob
from mrjob.step import MRStep

class CGPA(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_cgpa,
                   reducer=self.reducer_count_cgpa)
        ]

    def mapper_get_cgpa(self, _, line):
        (roll, cg) = line.split('\t')
	cgf = float(cg)
        if(cgf>=2.00 and cgf<2.50):
		yield "2.00 - 2.50", 1
	elif(cgf>=2.50 and cgf<3.00):
		yield "2.50 - 3.00", 1
	elif(cgf>=3.00 and cgf<3.50):
		yield "3.00 - 3.50", 1
	elif(cgf>=3.50 and cgf<=4.00):
		yield "3.50 - 4.00", 1

    def reducer_count_cgpa(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    CGPA.run()
