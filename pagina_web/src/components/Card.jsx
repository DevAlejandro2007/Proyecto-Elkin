export function Card({children, title="", classTitle="", className, img=null}) {
  return (
    <article className={`leading-relaxed bg-white flex flex-col tracking-wide p-8 ring-2 ring-black rounded-xl hover:scale-105 transition-all duration-300 ease-in-out hover:[&>*]:text-white space-y-2 ${className}`}>
    <h2 className={`text-lg font-semibold text-fuchsia-950 my-2 ${classTitle}`}>{title}</h2>
    <p>{children}</p>
    {img ? <img src={`${img}`} alt="" className="object-cover m-4 rounded-3xl border-3 border-black" /> : null }
    </article>
  )
}