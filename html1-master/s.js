
function myFunction(){
var url=window.location.href;
const uri=new URL(url);

document.getElementById("name").innerHTML=uri.searchParams.get("user")
}
