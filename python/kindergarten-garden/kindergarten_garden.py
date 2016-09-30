#create a Kindergarten Garden class, that maps a string representing plants on a windowsill to students who own them

default_students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
plant_mapping = {'C':'Clover','G':'Grass','R':'Radishes','V':'Violets'}

class Garden:
    def __init__(self, garden_string,students=None):
        if students is None:
            students = default_students
        self.garden_map = self._map_students(garden_string,students)

    def _map_students(self,garden_string,students):
        stud_list = sorted(students)
        gard_list = garden_string.split()
        mapping = {stud: [] for stud in stud_list}
        for idx, stud in enumerate(stud_list):
            if 2*idx > len(gard_list[0]) - 2:
                break
            mapping[stud] = [self._get_plant(gard_list[0][2*idx]),self._get_plant(gard_list[0][2*idx+1]),
                             self._get_plant(gard_list[1][2*idx]),self._get_plant(gard_list[1][2*idx+1])]
        return mapping

    def _get_plant(self,lst):
        return plant_mapping[lst]

    def plants(self,student):
        return self.garden_map[student]
