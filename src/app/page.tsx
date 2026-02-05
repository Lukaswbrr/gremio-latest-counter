"use client";

import { useState, useEffect } from 'react';

type MatchItem = {
    resultMatch?: string;
    resultString?: string;
};

export default function Home() {

    const [data, setData] = useState<MatchItem[]>([]);
    
    const getData = async () => {
        const response = await fetch("/api/scrape_test.py", {});
        const json = await response.json();

        setData(Array.isArray(json) ? (json as MatchItem[]) : []);
    }

    const testData = async () => {
        const response = await fetch("/api/scrape_test.py", {});
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
  
    useEffect(() => {
        getData();
    }, []);

  return (
    <div>
        <h1>Hello world!</h1>

        <button onClick={testData}>Fetch Data</button>

        {data.map((item, index: number) => (
            <div key={index}>
                <p>{item.resultMatch ?? item.resultString ?? ""}</p>
            </div>
        ))}
        
    </div>
  )
}
