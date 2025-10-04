"use client";
import { useState } from "react";
import brailleEnglish from "../../utils/brailleEnglish";
import brailleKannada from "../../utils/brailleKannada";

export default function Braille() {
  const [lang, setLang] = useState("english");
  const [text, setText] = useState("");

  const convertToBraille = () => {
    let mapping = lang === "english" ? brailleEnglish : brailleKannada;
    return text.split("").map(ch => mapping[ch.toLowerCase()] || ch).join(" ");
  };

  return (
    <main className="flex flex-col items-center p-8">
      <h1 className="text-3xl font-bold mb-4">Learn Braille</h1>

      <div className="flex gap-4 mb-6">
        <button
          onClick={() => setLang("english")}
          className={`px-4 py-2 rounded ${lang==="english" ? "bg-blue-600 text-white" : "bg-gray-200"}`}
        >
          English
        </button>
        <button
          onClick={() => setLang("kannada")}
          className={`px-4 py-2 rounded ${lang==="kannada" ? "bg-blue-600 text-white" : "bg-gray-200"}`}
        >
          Kannada
        </button>
      </div>

      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        className="w-80 h-32 p-3 border rounded-lg mb-6"
        placeholder={`Type ${lang} text here`}
      />

      <div className="w-80 p-4 bg-gray-100 rounded-lg shadow">
        <h2 className="text-lg font-semibold mb-2">Braille Output:</h2>
        <p className="text-2xl">{convertToBraille()}</p>
      </div>
    </main>
  );
}