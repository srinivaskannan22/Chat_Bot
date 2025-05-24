import logo from './logo.svg';
import './App.css';
import { useState } from 'react';


async function prompt2(prompt,bot){
 try{
  console.log(bot);
  const response=await fetch('http://localhost:8003/chatprompt',{
    method:'post',
    headers:{'content-type':'application/json'},
    
    body:JSON.stringify({
      item:prompt,
      model:bot

    })
  });
 const result=await response.json();
 console.log(result)
 return result;
 }catch(error){
  console.log(error)
  return error;
 }

}



function App() {
  const [bot,setbot]=useState('gemini');
  const [image,setimages]=useState('google-gemini-icon%20(1)');
  const message=document.querySelector('.message-context');
  function scrollbottom(){
    message.scrollTop=message.scrollHeight;
  }
  async function handleclick(){
    const prompt=document.getElementById('prompting').value;
    if(bot==='llama'){
      // try{
      //   document.getElementById('div_lama').style.display='none';
      // }catch{
      //   console.log("error");
      // }
      const div_gemini=document.createElement('div');
      div_gemini.className='div_gemini';
      const prompt_message=document.createElement('p');
      prompt_message.className='my-reply';
      prompt_message.innerHTML=prompt;
      prompt_message.style.backgroundColor='rgba(86, 86, 86, 0.97)';
      div_gemini.appendChild(prompt_message)
      console.log(prompt_message);
      if (message){
        message.appendChild(div_gemini);
      }else{
        console.log("error");
        return;
      }
      
      document.getElementById('prompting').value='';
      console.log(bot);
      const text=await prompt2(prompt,bot);
      // console.log(text);
      const text2=document.createElement('p');
      text2.className='model-reply'
      text2.innerHTML=text;
      text2.style.backgroundColor='rgba(234, 11, 11, 0.71)';
      div_gemini.appendChild(text2);
      if(message){
        message.appendChild(div_gemini);
      }
    }else{
      // try{
      //   document.getElementById('div_gemini').style.display='none';
      // }catch{
      //   console.log("error")
      // }
      
      const div_lama=document.createElement('div');
      div_lama.className='div_lama';
      const prompt_message=document.createElement('p');
      prompt_message.className='my-reply';
      prompt_message.innerHTML=prompt;
      prompt_message.style.backgroundColor='rgba(86, 86, 86, 0.97)';
      div_lama.appendChild(prompt_message)
      console.log(prompt_message);
      if (message){
        message.appendChild(div_lama);
      }else{
        console.log("error");
        return;
      }
      
      document.getElementById('prompting').value='';
      console.log(bot);
      const text=await prompt2(prompt,bot);
      // console.log(text);
      const text2=document.createElement('p');
      text2.className='model-reply'
      text2.innerHTML=text;
      text2.style.backgroundColor='rgba(234, 11, 11, 0.71)';
      div_lama.appendChild(text2);
      if(message){
        message.appendChild(div_lama);
      }

    }
    
    

  }
  return (
            <>
                <h1 className ='heading'>AI CHAT-BOT</h1>
                <div className="main-container">
                    <div className="conatiner1">
                        <div
                              className="gemini_logo"
                              onClick={(event) => {
                                setbot('gemini');
                                setimages('google-gemini-icon%20(1)');
                                try{
                                  document.querySelectorAll('.div_gemini').forEach(el => {
                                    el.style.display = 'none';
                                  });
                                  try{
                                    document.querySelectorAll('.div_lama').forEach(el => {
                                      el.style.display = 'block';
                                    });
                                  }catch{
                                    console.log('error')
                                  }
                                }catch{
                                  console.log('error');
                                };
                                
                    
                                event.target.style.backgroundColor = 'red';
                                setTimeout(() => {
                                  event.target.style.backgroundColor = 'rgba(49,118,38,.10)';
                                }, 300);
                              }}
                            >
                              <img src="images/google-gemini-icon%20(1).png" alt="gemini_logo_icon" srcSet="images/google-gemini-icon%20(1).png" />

                              <h3>Gemini Chat-Bot</h3>
                        </div>
                        <div className="gemini_logo" onClick={(event)=>{setbot('llama');setimages('llama');
                            try{
                                  document.querySelectorAll('.div_lama').forEach(el => {
                                    el.style.display = 'none';
                                  });
                                  try{
                                    document.querySelectorAll('.div_gemini').forEach(el => {
                                      el.style.display = 'block';
                                    });
                                  }catch{
                                    console.log('error')
                                  }
                                }catch{
                                  console.log('error');
                                };event.target.style.backgroundColor='red';setTimeout(()=>{event.target.style.backgroundColor='rgba(49,118,38,.10'},300)}}>
                            <img src="images/llama.png" alt="llama icon" srcSet='images/llama.png'/>
                            <h3>llama Chat-Bot</h3>
                        </div>
                    </div>
                    <div className="container2">
                        <div className="title_icon">
                            <img
                                  src={`images/${image}.png`}
                                  alt={image}
                                  srcSet={`images/${image}.png`}
                                />

                                <h2>{bot}</h2>
                        </div>
                        <div className ='message-context'></div>
                        <div className="search">
                            <form class='input-box'>
                                <input type="text" name="prompting" id="prompting" placeholder="prompting here" />
              
                                <input type="button"  id='button' onClick={handleclick} value="sumbit"/>

                            </form>
                        </div>
                  
                    </div>
                </div>
           </>     
    
    );
}

export default App;
