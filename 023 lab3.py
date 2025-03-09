class HeaterAgent:
    def __init__(self):
        self.previous_action = "off"
        self.low_threshold = 18
        self.high_threshold = 22

    def decide_action(self, current_temperature):
        if current_temperature < self.low_threshold and self.previous_action != "on":
            self.previous_action = "on"
            return "Turn heater ON"
        elif current_temperature > self.high_threshold and self.previous_action != "off":
            self.previous_action = "off"
            return "Turn heater OFF"
        else:
            return f"Keep heater {self.previous_action.upper()}"

def simulate_heater_agent():
    agent = HeaterAgent()
    temperatures = [20, 17, 19, 23, 16, 25, 18, 21]

    for temp in temperatures:
        action = agent.decide_action(temp)
        print(f"Temperature: {temp}°C -> Action: {action}")

simulate_heater_agent()