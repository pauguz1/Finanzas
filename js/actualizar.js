function actualizarPaso1(id){
    var paso=document.getElementById('contenedorActualizar');
    paso.innerHTML=`
        <div class="close"> <Button onclick="closePanel('${id}')">X</Button> </div>
        <div class="row mt-3 col-md-6 d-flex justify-content-center">
          <h1>Ventas</h1>
        </div>
  
        <div class="row pt-4 pb-4  ml-0 mr-0 pl-0 pr-0 col-md-12 d-flex  justify-content-center rounded ">
    
          <div class="row col-md-12 mt-1 mb-1 d-flex d-flex justify-content-center inputDatos">
            <h5 class="pl-0 pr-0 text-center col-md-6">Devoluciones ventas</h5>
            <input class="ml-1 mr-1" type="text">
           <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
          </div>
  
          <div class="row col-md-12 mt-1 mb-1 d-flex justify-content-center inputDatos">
             <h5 class="pl-0 pr-0 text-center col-md-6">Descuentos en ventas</h5>
             <input class="ml-1 mr-1" type="text">
             <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
          </div>
  
          <div class="row col-md-12 mt-1 mb-1 d-flex  justify-content-center inputDatos">
           <h5 class="pl-0 pr-0 text-center col-md-6">Bonif y reb en ventas</h5>
           <input class="ml-1 mr-1" type="text">
           <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
          </div>
  
          <div class="row col-md-12 mt-3 mb-3  d-flex justify-content-center inputDatos">
           <button class="col-md-12 btn colorSave boton" onclick="crearMensaje1('1','p1')">Guardar</button>
          </div>
      </div>
    `;
    var elemento=document.getElementById(String(id));
  elemento.focus();
  }

  function actualizarPaso2(id){
    var paso=document.getElementById('contenedorActualizar');
    paso.innerHTML=`
        <div class="close"> <Button onclick="closePanel('${id}')">X</Button> </div>
        <div class="row mt-3 col-md-6 d-flex justify-content-center">
          <h1>Ventas Devoluciones</h1>
        </div>
  
        <div class="row pt-4 pb-4  ml-0 mr-0 pl-0 pr-0 col-md-12 d-flex  justify-content-center rounded ">
    
          <div class="row col-md-12 mt-1 mb-1 d-flex d-flex justify-content-center inputDatos">
            <h5 class="pl-0 pr-0 text-center col-md-6">Devoluciones ventas</h5>
            <input class="ml-1 mr-1" type="text">
           <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
          </div>
  
          <div class="row col-md-12 mt-1 mb-1 d-flex justify-content-center inputDatos">
             <h5 class="pl-0 pr-0 text-center col-md-6">Descuentos en ventas</h5>
             <input class="ml-1 mr-1" type="text">
             <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
          </div>
  
          <div class="row col-md-12 mt-1 mb-1 d-flex  justify-content-center inputDatos">
           <h5 class="pl-0 pr-0 text-center col-md-6">Bonif y reb en ventas</h5>
           <input class="ml-1 mr-1" type="text">
           <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
          </div>
  
          <div class="row col-md-12 mt-3 mb-3  d-flex justify-content-center inputDatos">
           <button class="col-md-12 btn colorSave boton" onclick="crearMensaje1('1','p1')">Guardar</button>
          </div>
      </div>
    `;
    var elemento=document.getElementById(String(id));
  elemento.focus();
  }


  const $btnCargarPerfil = document.querySelector("#agregar"),
    $perfil = document.querySelector("#agregar");
$btnCargarPerfil.addEventListener("click", () => {
    fetch("http://127.0.0.1:8000/getBalance")
        .then(respuesta => respuesta.text())
        .then(respuestaComoHTML => {
            $perfil.innerHTML = respuestaComoHTML;
        });
});