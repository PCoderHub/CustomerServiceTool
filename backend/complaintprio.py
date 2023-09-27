#priority class for complaint

from concernpriority import ConcernPriority

class ComplaintPrio(ConcernPriority):
    def prioset(self):
        prio = "high"
        return prio