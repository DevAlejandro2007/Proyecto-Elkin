export async function upForm(formData=null){

    if(!formData){
        return { error: "Datos invalidos" };
    }

  fetch("data/login", { 
    method: "POST",

  })
}