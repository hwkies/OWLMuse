"use client";
import { Input } from "@chakra-ui/react";

interface CustomInputProps extends Omit<React.InputHTMLAttributes<HTMLInputElement>, "size"> {
  className?: string;
  size?: "sm" | "md" | "lg" | "xl" | "2xl" | "2xs" | "xs";
}

export default function CustomInput({
  className,
  size,
  children,
  ...props
}: CustomInputProps) {
  const defaultCn =
    "px-2 border-2 border-primary dark:border-primary-dark text-background-dark dark:text-background";
  const cn = className ? `${className} ${defaultCn}` : defaultCn;

  return <Input size={size} {...props} className={cn}>{children}</Input>;
}