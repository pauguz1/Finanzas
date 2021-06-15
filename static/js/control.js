    var btn1=document.getElementById('paso1');
    var btn2=document.getElementById('paso2');
    var btn3=document.getElementById('paso3');
    var btn4=document.getElementById('paso4');
    var btn5=document.getElementById('paso5');
    var btn6=document.getElementById('paso6');
    var btn7=document.getElementById('paso7');

    var contenido=document.getElementById('pasoX');
    //----------------- Mensajes en pantalla    -------------------------------------------------------------------------


    /* Crea un mensaje con titulo, descripcion y Video */
    /* Crea un mensaje con solo el titulo */
    function crearMensaje1(id,titulo){
      var men=document.getElementById("bodu");
      men.innerHTML+=`
      <div id="${id}" class="fondo d-flex justify-content-center" onkeydown="borrar('${id}')" tabindex="-1">
      <div class="contenedorMensaje col-sm-12 col-md-4 ml-2 mr-2  d-flex justify-content-center">
    <div class="close"> <Button onclick="closePanel('${id}')">X</Button> </div>
    <div class="titulo"> <h1>${titulo}</h1> </div>
    <div class="descripcion">
    </div>
  </div></div>`;
  var elemento=document.getElementById(String(id));
  elemento.focus();
    }

    /* Crea un mensaje con titulo y descipcion */
    function crearMensaje2(id,titulo,descripcion){
      var men=document.getElementById("bodu");
      men.innerHTML+=`
      <div id="${id}" class="fondo d-flex justify-content-center" onkeydown="borrar('${id}')" tabindex="-1">
      <div class="contenedorMensaje col-sm-12 col-md-4 ml-2 mr-2  d-flex justify-content-center">
    <div class="close"> <Button onclick="closePanel('${id}')">X</Button> </div>
    <div class="titulo"> <h1>${titulo}</h1> </div>
    <div class="descripcion">
      <p>${descripcion}</p>
    </div>
  </div></div>`;
  var elemento=document.getElementById(String(id));
  elemento.focus();
    }
    

    /* Crea un mensaje con titulo, descripcion y Video */
    function crearMensaje3(id,titulo,descripcion,urlVideo){
      var men=document.getElementById("bodu");
      men.innerHTML+=`
      <div id="${id}" class="fondo d-flex justify-content-center" onkeydown="borrar('${id}')" tabindex="-1">
      <div class="contenedorMensaje col-sm-12 col-md-4 ml-2 mr-2  d-flex justify-content-center">
    <div class="close"> <Button onclick="closePanel('${id}')">X</Button> </div>
    <div class="titulo"> <h1>${titulo}</h1> </div>
    <div class="descripcion">
      <p>${descripcion}</p>
    </div>
    <iframe class="video" src="${urlVideo}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  </div></div>`;
  var elemento=document.getElementById(String(id));
  elemento.focus();


    }


/** Eliminar el Nodo */
    function closePanel(ventana){
      var ventana1=document.getElementById(String(ventana));
      ventana1.remove();
    }
    var bandera=true;
    function presionado(){
      
      var boton=document.getElementById('paso1');
      if(Boolean(bandera)){
        boton.innerHTML=`<h1>Ventas</h1>`;
        bandera=false;
      }else{
        boton.innerHTML=`<h1>1</h1>`;
        bandera=true;
      }
    }


      function borrar(id){
        console.log(window.event.code);
        var tecla=window.event.code;
        if (tecla === 'Escape' || tecla === 27) {
         closePanel(id);
       }
      }
//-------------------------------------------------------------------------------------------------------------------------------
    function pasoX1(){
      contenido.innerHTML=`
      <div class="row offset-3 mt-3 col-md-6 justify-content-center">
    <h1>Ventas</h1>
  </div>
  
  <div class="row pt-4 pb-4 pl-0 pr-0 jumbotron offset-4 col-md-4  justify-content-center dark">
    
    <div class="row col-md-12 mt-1 mb-1 align-items-center justify-content-center inputDatos">
      <h5 class="pl-0 pr-0 text-center col-md-6">Devoluciones ventas</h5>
      <input class="ml-1 mr-1" type="text">
      <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
    </div>
  
    <div class="row col-md-12 mt-1 mb-1 align-items-center justify-content-center inputDatos">
      <h5 class="pl-0 pr-0 text-center col-md-6">Descuentos en ventas</h5>
      <input class="ml-1 mr-1" type="text">
      <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
    </div>
  
    <div class="row col-md-12 mt-1 mb-1 align-items-center justify-content-center inputDatos">
      <h5 class="pl-0 pr-0 text-center col-md-6">Bonif y reb en ventas</h5>
      <input class="ml-1 mr-1" type="text">
      <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
    </div>
  
    <div class="row col-md-12 mt-3 mb-3 align-items-center justify-content-center inputDatos">
      <button class="col-md-3 btn colorSave">Guardar</button>
    </div>
  
    
  </div>
      `;
    }

    function pasoX2(){
      contenido.innerHTML=`
      <div class="row offset-3 mt-3 col-md-6 justify-content-center">
  <h1>inventario inicial mercancia </h1>
</div>

<div class="row pt-4 pb-4 pl-0 pr-0 jumbotron offset-4 col-md-4  justify-content-center dark">
  
  <div class="row col-md-12 mt-1 mb-1 align-items-center justify-content-center inputDatos">
    <h5 class="pl-0 pr-0 text-center col-md-6">compras</h5>
    <input class="ml-1 mr-1" type="text">
    <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
  </div>

  <div class="row col-md-12 mt-1 mb-1 align-items-center justify-content-center inputDatos">
    <h5 class="pl-0 pr-0 text-center col-md-6">fletes de compras</h5>
    <input class="ml-1 mr-1" type="text">
    <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
  </div>

  <div class="row col-md-12 mt-1 mb-1 align-items-center justify-content-center inputDatos">
    <h5 class="pl-0 pr-0 text-center col-md-6">gastos de importacion</h5>
    <input class="ml-1 mr-1" type="text">
    <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
  </div>

  <div class="row col-md-12 mt-3 mb-3 align-items-center justify-content-center inputDatos">
    <button class="col-md-3 btn colorSave">Guardar</button>
  </div>

  
</div>
      `;
    }
    function pasoX3(){
      contenido.innerHTML=`
      <div class="row offset-3 mt-3 col-md-6 justify-content-center">
  <h1>Monto Total De Compras </h1>
</div>

<div class="row pt-4 pb-4 pl-0 pr-0 jumbotron offset-4 col-md-4  justify-content-center dark">
  
  <div class="row col-md-12 mt-1 mb-1 align-items-center justify-content-center inputDatos">
    <h5 class="pl-0 pr-0 text-center col-md-6">devoluciones en compras</h5>
    <input class="ml-1 mr-1" type="text">
    <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
  </div>

  <div class="row col-md-12 mt-1 mb-1 align-items-center justify-content-center inputDatos">
    <h5 class="pl-0 pr-0 text-center col-md-6">descuentos en compras</h5>
    <input class="ml-1 mr-1" type="text">
    <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
  </div>

  <div class="row col-md-12 mt-1 mb-1 align-items-center justify-content-center inputDatos">
    <h5 class="pl-0 pr-0 text-center col-md-6">bonificacion en compras</h5>
    <input class="ml-1 mr-1" type="text">
    <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
  </div>

  <div class="row col-md-12 mt-1 mb-1 align-items-center justify-content-center inputDatos">
    <h5 class="pl-0 pr-0 text-center col-md-6">compras netas</h5>
    <input class="ml-1 mr-1" type="text">
    <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
  </div>

  <div class="row col-md-12 mt-1 mb-1 align-items-center justify-content-center inputDatos">
    <h5 class="pl-0 pr-0 text-center col-md-6">mercancia disponible para la venta</h5>
    <input class="ml-1 mr-1" type="text">
    <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
  </div>

  
  <div class="row col-md-12 mt-1 mb-1 align-items-center justify-content-center inputDatos">
    <h5 class="pl-0 pr-0 text-center col-md-6">inventario final</h5>
    <input class="ml-1 mr-1" type="text">
    <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
  </div>

  <div class="row col-md-12 mt-1 mb-1 align-items-center justify-content-center inputDatos">
    <h5 class="pl-0 pr-0 text-center col-md-6">costo de venta</h5>
    <input class="ml-1 mr-1" type="text">
    <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
  </div>
  
  <div class="row col-md-12 mt-3 mb-3 align-items-center justify-content-center inputDatos">
    <button class="col-md-3 btn colorSave">Guardar</button>
  </div>

  
</div>
      `;
    }
    function pasoX4(){
      contenido.innerHTML=`
      <div class="row offset-3 mt-3 col-md-6 justify-content-center">
  <h1>Gastos de ventas </h1>
</div>

<div class="row pt-4 pb-4 pl-0 pr-0 jumbotron offset-4 col-md-4  justify-content-center dark">
  
  <div class="row col-md-12 mt-1 mb-1 align-items-center justify-content-center inputDatos">
    <h5 class="pl-0 pr-0 text-center col-md-6">sueldo  de vendedore</h5>
    <input class="ml-1 mr-1" type="text">
    <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
  </div>

  <div class="row col-md-12 mt-1 mb-1 align-items-center justify-content-center inputDatos">
    <h5 class="pl-0 pr-0 text-center col-md-6">comisiones sobre venta</h5>
    <input class="ml-1 mr-1" type="text">
    <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
  </div>

  <div class="row col-md-12 mt-1 mb-1 align-items-center justify-content-center inputDatos">
    <h5 class="pl-0 pr-0 text-center col-md-6">propaganda</h5>
    <input class="ml-1 mr-1" type="text">
    <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
  </div>

  <div class="row col-md-12 mt-1 mb-1 align-items-center justify-content-center inputDatos">
    <h5 class="pl-0 pr-0 text-center col-md-6">impuesto municipales</h5>
    <input class="ml-1 mr-1" type="text">
    <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
  </div>

  <div class="row col-md-12 mt-1 mb-1 align-items-center justify-content-center inputDatos">
    <h5 class="pl-0 pr-0 text-center col-md-6">total de gastos de ventas</h5>
    <input class="ml-1 mr-1" type="text">
    <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
  </div>


  <div class="row col-md-12 mt-3 mb-3 align-items-center justify-content-center inputDatos">
    <button class="col-md-3 btn colorSave">Guardar</button>
  </div>

  
</div>
      `;
    }
    function pasoX5(){
      contenido.innerHTML=`
      <div class="row offset-3 mt-3 col-md-6 justify-content-center">
  <h1>Gastos administrativos </h1>
</div>

<div class="row pt-4 pb-4 pl-0 pr-0 jumbotron offset-4 col-md-4  justify-content-center dark">
  
  <div class="row col-md-12 mt-1 mb-1 align-items-center justify-content-center inputDatos">
    <h5 class="pl-0 pr-0 text-center col-md-6">gastos de alquiler</h5>
    <input class="ml-1 mr-1" type="text">
    <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
  </div>

  <div class="row col-md-12 mt-1 mb-1 align-items-center justify-content-center inputDatos">
    <h5 class="pl-0 pr-0 text-center col-md-6">gasto generales</h5>
    <input class="ml-1 mr-1" type="text">
    <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
  </div>

  <div class="row col-md-12 mt-1 mb-1 align-items-center justify-content-center inputDatos">
    <h5 class="pl-0 pr-0 text-center col-md-6">sueldo de los de administracion</h5>
    <input class="ml-1 mr-1" type="text">
    <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
  </div>

  <div class="row col-md-12 mt-1 mb-1 align-items-center justify-content-center inputDatos">
    <h5 class="pl-0 pr-0 text-center col-md-6">perdidasen cuentas malas</h5>
    <input class="ml-1 mr-1" type="text">
    <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
  </div>

  <div class="row col-md-12 mt-1 mb-1 align-items-center justify-content-center inputDatos">
    <h5 class="pl-0 pr-0 text-center col-md-6">total de gastos de administracion</h5>
    <input class="ml-1 mr-1" type="text">
    <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
  </div>


  <div class="row col-md-12 mt-3 mb-3 align-items-center justify-content-center inputDatos">
    <button class="col-md-3 btn colorSave">Guardar</button>
  </div>

  
</div>
      `;
    }
    function pasoX6(){
      contenido.innerHTML=`
      <div class="row offset-3 mt-3 col-md-6 justify-content-center">
  <h1>Otros Ingresos </h1>
</div>

<div class="row pt-4 pb-4 pl-0 pr-0 jumbotron offset-4 col-md-4  justify-content-center dark">
  
  <div class="row col-md-12 mt-1 mb-1 align-items-center justify-content-center inputDatos">
    <h5 class="pl-0 pr-0 text-center col-md-6">alquileres ganados</h5>
    <input class="ml-1 mr-1" type="text">
    <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
  </div>

  <div class="row col-md-12 mt-1 mb-1 align-items-center justify-content-center inputDatos">
    <h5 class="pl-0 pr-0 text-center col-md-6">intereses ganadoas</h5>
    <input class="ml-1 mr-1" type="text">
    <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
  </div>

  <div class="row col-md-12 mt-1 mb-1 align-items-center justify-content-center inputDatos">
    <h5 class="pl-0 pr-0 text-center col-md-6">comisiones ganados</h5>
    <input class="ml-1 mr-1" type="text">
    <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
  </div>

  <div class="row col-md-12 mt-1 mb-1 align-items-center justify-content-center inputDatos">
    <h5 class="pl-0 pr-0 text-center col-md-6">Total de ingresos</h5>
    <input class="ml-1 mr-1" type="text">
    <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
  </div>


  <div class="row col-md-12 mt-3 mb-3 align-items-center justify-content-center inputDatos">
    <button class="col-md-3 btn colorSave">Guardar</button>
  </div>

  
</div>
      `;
    }
    function pasoX7(){
      contenido.innerHTML=`
      <div class="row offset-3 mt-3 col-md-6 justify-content-center">
  <h1>Otros Engresos </h1>
</div>

<div class="row pt-4 pb-4 pl-0 pr-0 jumbotron offset-4 col-md-4  justify-content-center dark">
  
  <div class="row col-md-12 mt-1 mb-1 align-items-center justify-content-center inputDatos">
    <h5 class="pl-0 pr-0 text-center col-md-6">intereses gastos</h5>
    <input class="ml-1 mr-1" type="text">
    <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
  </div>

  <div class="row col-md-12 mt-1 mb-1 align-items-center justify-content-center inputDatos">
    <h5 class="pl-0 pr-0 text-center col-md-6">perdidas en ventas</h5>
    <input class="ml-1 mr-1" type="text">
    <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
  </div>

  <div class="row col-md-12 mt-1 mb-1 align-items-center justify-content-center inputDatos">
    <h5 class="pl-0 pr-0 text-center col-md-6">total de otros egresos</h5>
    <input class="ml-1 mr-1" type="text">
    <a class="ml-1 mr-1 h5" href="#" title="Información adicional">?</a>
  </div>

  <div class="row col-md-12 mt-3 mb-3 align-items-center justify-content-center inputDatos">
    <button class="col-md-3 btn colorSave">Guardar</button>
  </div>
</div>
      `;
    }


    /* Crea un mensaje con solo el titulo */
    function mostrarPaso(id,paso){
      var men=document.getElementById("bodu");
      men.innerHTML+=`
      <div id="${id}" class="fondo d-flex justify-content-center" onkeydown="borrar('${id}')" tabindex="-1">

      <!-- Barra lateral -->
      <div class="fixed1 front">
        <div class="contenido borde1" id="paso1" onclick="actualizarPaso1('${id}')" ><h1>1</h1></div>
        <div class="contenido" id="paso2" onclick="actualizarPaso2('${id}')"><h1>2</h1></div>
        <div class="contenido" id="paso3" onclick="actualizarPaso3('${id}')"><h1>3</h1></div>
        <div class="contenido" id="paso4" onclick="actualizarPaso4('${id}')"><h1>4</h1></div>
        <div class="contenido" id="paso5" onclick="actualizarPaso5('${id}')"><h1>5</h1></div>
        <div class="contenido" id="paso6" onclick="actualizarPaso6('${id}')"><h1>6</h1></div>
        <div class="contenido borde2" id="paso7" onclick="actualizarPaso7  ('${id}')"><h1>7</h1></div>
      </div>
      <!-- Fin Barra lateral -->


      <div id="contenedorActualizar" class="contenedorMensaje dark col-sm-12 col-md-4  d-flex justify-content-center"> 
      

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
    </div>
  </div>
  
  `;
  var elemento=document.getElementById(String(id));
  elemento.focus();
    }
   // mostrarPaso('1',"Venta")
  
    //crearMensaje3("p1","Ventas","informacion referente a ventas","https://www.youtube.com/embed/LBagGr5iFHU");