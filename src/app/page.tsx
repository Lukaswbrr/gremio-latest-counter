"use client";

export default function Home() {
  
  const testData = async () => {
      const response = await fetch("api/scrape_test.py", {});
      const data = await response.json();

      console.log(data);
  }
  
  return (
      <div>
          <h1>Hello world!</h1>

          <button onClick={testData}>Fetch Data</button>
      </div>
      
  )
}
