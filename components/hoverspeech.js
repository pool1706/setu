"use client";
import { useEffect } from "react";

export default function HoverSpeech() {
  useEffect(() => {
    const elements = document.querySelectorAll("[data-speak]");

    elements.forEach(el => {
      el.addEventListener("mouseenter", () => {
        const text = el.getAttribute("data-speak");
        if (window.speechSynthesis) {
          const msg = new SpeechSynthesisUtterance(text);
          window.speechSynthesis.speak(msg);
        }
      });
    });
  }, []);

  return null; // invisible helper component
}