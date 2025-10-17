export function Card({children, className}) {
  return (
    <article className={`leading-relaxed tracking-wide p-6 ring-2 ring-black rounded-xl h-auto hover:scale-105 transition-all duration-300 ease-in-out hover:[&>p]:text-white hover:[&>h2]:text-white ${className}`}>{children}</article>
  )
}
