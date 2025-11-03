export function Card({children, title="", className="", img=null}) {
  return (
    <article className={`leading-relaxed flex flex-col tracking-wide p-8 ring-2 ring-black rounded-xl transition-all duration-300 ease-in-out space-y-2 [&>p]:text-white ${className}`}>
    <h2 className={`text-lg text-white font-semibold my-2 leading-relaxed tracking-wide`}>{title}</h2>
    <p>{children}</p>
    {img ? <img src={`${img}`} alt="" className="size-3/5 self-center border-2 border-black mt-8" /> : null }
    </article>
  )
}