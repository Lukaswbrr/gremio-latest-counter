"use client";

import { match } from "assert";

export default function Home() {
  
  const testData = async () => {
      const response = await fetch("api/scrape_test.py", {});
      const data = await response.json();

      console.log(data);

      for (const item of data) {
          switch (item.resultString) {
            case "W":
                console.log("Win");
                break;
            case "L":
                console.log("Loss");
                break;
            case "D":
                console.log("Draw");
                break;
            default:
                console.log("Unknown result");
          }
      }

      return data;
  }
  
  return (
      <div>
          <h1>Hello world!</h1>

          <button onClick={testData}>Fetch Data</button>

          <div className="stats">
                {/* Stats will be displayed here */}
                {testData().then(data => 
                    data.map((item: { resultString: string }, index: number) =>
                    <div key={index}>
                        <p>Result: {item.resultString}</p>
                    </div>
                ))}
          </div>
      </div>
      
  )
}
