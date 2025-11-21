export function P({children, className=""}) {
  return (
    <p className={`leading-relaxed tracking-wide text-lg ${className}`}>{children}</p>
  )
}
