"use client";
import Image from "next/image";
import { useState } from "react";

export default function Sign() {
  const [letter, setLetter] = useState("a");

  return (
    <main className="flex flex-col items-center p-8">
      <h1 className="text-3xl font-bold mb-4">Learn Kannada Sign Language</h1>
      <p className="mb-6 text-gray-700">Select a letter to see its sign representation.</p>

      <input 
        type="text" 
        maxLength="1" 
        value={letter} 
        onChange={(e) => setLetter(e.target.value.toLowerCase())} 
        className="border p-2 rounded mb-6 text-center"
      />

      <div className="w-64 h-64 flex items-center justify-center bg-gray-100 rounded-lg shadow">
        <Image 
          src={`/isl/${letter}.png`} 
          alt={`Sign for ${letter}`} 
          width={200} 
          height={200}
        />
      </div>
    </main>
  );
}