import { Input } from "@chakra-ui/react"

interface CustomInputProps extends React.AnchorHTMLAttributes<HTMLAnchorElement> {
  type: string;
  value: string;
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
  required: boolean;
  className?: string;
}

export default function CustomInput({ type, value, onChange, required, className, children, ...props }: CustomLinkProps) {
  const defaultCn = "px-2 border-2 border-primary dark:border-primary-dark text-background-dark dark:text-background"
  const cn = className ? ` ${className} ` + defaultCn : defaultCn;
  return (
    <Input type={type} value={value} onChange={onChange} required={required} {...props} className={cn}>
      {children}
    </Input>
  );
}