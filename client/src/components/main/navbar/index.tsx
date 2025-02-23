import * as React from "react"
import { Input } from "@chakra-ui/react"
import Link from "next/link"
import { ColorModeButton } from "@/components/ui/color-mode"

const NavBar = () => {

  return (
    <nav className="grid grid-cols-3 items-center px-4 py-2 border-b-2 bg-secondary dark:bg-secondary-dark border-b-foreground dark:border-b-foreground-dark text-foreground dark:text-foreground-dark">
      <div className="justify-self-start">
        <Link href="/" className="font-bold text-2xl">
          OWLMuse
        </Link>
      </div>
      <div className="justify-self-center min-w-full">
        <Input placeholder="Search for overwatch statistics" className="bg-white px-3 rounded-2xl" />
      </div>
      <div className="justify-self-end flex items-center">
        <Link href="/login" className="font-semibold px-3 py-1 rounded-lg mr-1 text-xl border-2 border-foreground dark:border-foreground-dark hover:bg-foreground hover:text-background dark:hover:bg-foreground-dark dark:hover:text-background-dark">
          Log In
        </Link>
        <Link href="/signup" className="font-semibold px-3 py-1 rounded-lg ml-1 text-xl border-2 border-foreground dark:border-foreground-dark hover:bg-foreground hover:text-background dark:hover:bg-foreground-dark dark:hover:text-background-dark">
          Sign Up
        </Link>
        <ColorModeButton className="ml-2" />
      </div>
    </nav>
  );
}

export default NavBar;