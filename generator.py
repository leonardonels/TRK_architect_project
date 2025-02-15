import pandas as pd
import subprocess
import random
import math

class Generator:

    visualize = True
    turn_propability = 0.75

    def decision(self, probability):
        return random.random() < probability

    def compute_point_c(self, A, B, theta_rad):
        Vx = B['x'] - A['x']
        Vy = B['y'] - A['y']

        cos_theta = math.cos(theta_rad)
        sin_theta = math.sin(theta_rad)

        new_Vx = Vx * cos_theta - Vy * sin_theta
        new_Vy = Vx * sin_theta + Vy * cos_theta

        C_x = B['x'] + new_Vx
        C_y = B['y'] + new_Vy

        return (C_x, C_y)

    def main(self):
        try:
            starting_points=[{'x':0.0, 'y':0.0},{'x':0.0, 'y':0.5}]
            df=pd.DataFrame(starting_points)

            for i in range(98):
                if self.decision(self.turn_propability):
                    new_p = self.compute_point_c(df.iloc[i], df.iloc[i+1], random.uniform(-3.14/6,3.14/6))
                else:
                    new_p = self.compute_point_c(df.iloc[i], df.iloc[i+1], random.uniform(-3.14/3,3.14/3))
                df.loc[i+2]={'x':new_p[0],'y':new_p[1]}
            
            df.to_csv("generated_track.csv", index=False)

            if self.visualize:
                subprocess.run(["python3",
                                        "utils/track_visualizer.py",
                                        "--track", "generated_track.csv",
                                        ], check=True)

            pass
        except KeyboardInterrupt:
            pass

if __name__ == '__main__':
    generator = Generator()
    generator.main()