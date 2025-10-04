import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="flex justify-between items-center p-4 bg-gray-100 shadow">
      <Link href="/" className="text-2xl font-bold">
        Setu
      </Link>
      <div className="flex gap-6">
        <Link href="/braille" className="hover:text-blue-600">
          Braille
        </Link>
        <Link href="/sign" className="hover:text-green-600">
          Sign Language
        </Link>
      </div>
    </nav>
  );
}