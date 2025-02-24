import Link from "next/link";

interface CustomLinkProps extends React.AnchorHTMLAttributes<HTMLAnchorElement> {
  href: string;
  className?: string;
}

export default function CustomLink({ href, className, children, ...props }: CustomLinkProps) {
  const defaultCn = "border-2 border-primary dark:border-primary-dark hover:bg-primary hover:text-background dark:hover:bg-primary-dark dark:hover:text-background-dark"
  const cn = className ? ` ${className} ` + defaultCn : defaultCn;
  return (
    <Link href={href} {...props} className={cn}>
      {children}
    </Link>
  );
}
