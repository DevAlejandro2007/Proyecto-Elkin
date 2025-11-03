export function Input({ className="", ...props }) {
  return (
    <input {...props} className={`text-black placeholder-gray-500 px-2 ring-1 ring-black focus:ring-2 w-3/4 rounded-sm py-1.5 select-none ${className}`} />

  )
}
