export default function Home() {
  return (
    <main className="flex flex-col items-center justify-center min-h-screen p-8">
      <h1 className="text-4xl font-bold mb-6">Setu</h1>
      <p className="text-lg text-center max-w-2xl mb-8">
        A minimalistic app to help differently-abled people learn 
        <strong> Sign Language </strong> and <strong> Braille </strong> 
        in English and Kannada.
      </p>

      <div className="flex gap-6">
        <a 
          href="/braille" 
          className="px-6 py-3 bg-blue-600 text-white rounded-xl shadow hover:bg-blue-700 transition"
        >
          Learn Braille
        </a>
        <a 
          href="/sign" 
          className="px-6 py-3 bg-green-600 text-white rounded-xl shadow hover:bg-green-700 transition"
        >
          Learn Sign Language
        </a>
      </div>
    </main>
  );
}