
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    
    # Read data from file
    data = open('results.txt')
    raw_data = data.readlines()
    data.close()

    # Create output
    out = open('out.txt', 'w')
    out.write('min,max,average\n')

    # Find the min/max/average
    for i in range(0, len(raw_data)):
        if (i % 15) == 13:
            text = ""
            for part in raw_data[i].split(','):
                for char in part:
                    if char.isdigit():
                        text = text + char
                text = text + ','
            
            text = text.rstrip(',') + '\n'
            out.write(text)
    
    # Done with output
    out.close()

    # Create plots
    DTA = pd.read_csv("out.txt")
 
    print("Min Ping: " + str(min(DTA["min"])))
    print("Max Ping: " + str(max(DTA["max"])))

    for item in ["min", "max", "average"]:
        unique, counts = np.unique(DTA[item], return_counts=True)

        plt.figure(figsize=(20,20))


        plt.title(item)
        plt.ylabel("Count")
        plt.xlabel("Ping (ms)")
        
        plt.scatter(unique, counts)

        #patches, texts, pct = plt.pie(x=counts, autopct="%.2f%%")
        #plt.legend(patches, unique)
        
        plt.show()

main()
