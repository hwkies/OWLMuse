import * as React from "react"
import { Input } from "@chakra-ui/react"
import Link from "next/link"
import CustomLink from "@/components/ui/custom-link";
import { ColorModeButton } from "@/components/ui/color-mode"

const NavBar = () => {

  return (
    <nav 
      className="grid grid-cols-3 items-center px-4 py-2 border-b-2 border-b-primary dark:border-b-primary-dark">
      <div className="justify-self-start">
        <Link href="/" className="font-bold text-2xl">
          OWLMuse
        </Link>
      </div>
      <div className="justify-self-center min-w-full">
        <Input 
          placeholder="Search for overwatch statistics" 
          className="px-3 rounded-2xl border-2 border-primary dark:border-primary-dark text-background-dark dark:text-background" />
      </div>
      <div className="justify-self-end flex justify-around items-center">
        <CustomLink 
          href="/login" 
          className="font-semibold px-3 py-1 rounded-lg text-xl mr-1">
          Log In
        </CustomLink>
        <CustomLink 
          href="/signup" 
          className="font-semibold px-3 py-1 rounded-lg text-xl ml-1">
          Sign Up
        </CustomLink>
        <ColorModeButton className="ml-2" />
      </div>
    </nav>
  );
}

export default NavBar;