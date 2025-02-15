import matplotlib.pyplot as plt
import pandas as pd
import argparse

def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('--track', type=str, 
                           default='generated_track.csv',
                           help='Path to generated_track.csv')
        
        args = parser.parse_args()

        df=pd.read_csv(args.track)

        df=df[::-1].reset_index(drop=True)

        plt.figure(figsize=(12, 8))
        plt.scatter(df['x'], df['y'], color='blue', label="line")

        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Scatter Plot of coordinates X-Y")
        plt.legend()
        plt.grid(True)

        plt.show()

    except KeyboardInterrupt:
        plt.close('all')
        return

if __name__ == "__main__":
    main()