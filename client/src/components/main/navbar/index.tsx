import * as React from "react"
import { Input } from "@chakra-ui/react"
import Link from "next/link"

const NavBar = () => {
  return (
    <nav className="bg-cyan-500 grid grid-cols-3 items-center px-4 py-2">
      <div className="justify-self-start">
        <Link href="/" className="text-white font-bold text-2xl">
          OWLMuse
        </Link>
      </div>
      <div className="justify-self-center min-w-full">
        <Input placeholder="Search for overwatch statistics" className="bg-white px-3 rounded-2xl border-4" />
      </div>
      <div className="justify-self-end">
        <Link href="/login" className="text-white font-semibold text-2xl">Log In</Link>
        <span className="text-white font-semibold text-3xl"> | </span>
        <Link href="/signup" className="text-white font-semibold text-2xl">Sign Up</Link>
      </div>
    </nav>
  );
}

export default NavBar;