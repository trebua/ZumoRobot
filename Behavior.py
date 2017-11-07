
class Behavior:

    def __init__(self, bbcon, priority = 0):
        self.bbcon = bbcon  # pointer to the controller that uses this behavior.
        self.sensobs = []   #a list of all sensobs that this behavior uses
        self.motor_recommendations = [] #list of motor recommendations for arbitrator
        self.active_flag = False    #active/inactive behavior
        self.priority = priority #Initial priority
        self.weight = 0

    def set_priority(self,priority):
        self.priority = priority

    def consider_deactivation(self):
        if self.active_flag:
            #consider deactivation
            pass

    def consider_activation(self):
        if not self.active_flag:
            #consider activation
            pass

    def sense_and_act(self):
        pass
        

    def update(self):
        for sensor in self.sensobs:
            sensor.update()


        pass

    def add_sensob(self,sensob):
        self.sensobs.append(sensob)

    def add_motor_recommendation(self,motor_recommendation):
        self.motor_recommendations.append(motor_recommendation)