import { H2 } from "./ui/H2";

export function Card({children, title="", className="", img=null}) {
  return (
    <article className={`leading-relaxed flex flex-col tracking-wide p-8 rounded-xl transition-all duration-300 ease-in-out space-y-3 ring-2 ring-black bg-neutral-100 ${className}`}>
    <H2>{title}</H2>
    <p>{children}</p>
    <div className="h-1/2 w-full items-center flex flex-1 justify-center">
    {img ? <img src={`${img}`} alt="" className="self-center object-cover size-[80%] object-[20%_70%]" /> : null }
    </div>
    </article>
  )
}