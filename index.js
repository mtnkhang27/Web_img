import {PyScript} from 

function submitFunction(){
  async function runPythonScript(scriptPath) {
    const pyScript = await new pyscript.PyScript();
    await pyScript.load(scriptPath);
    const output = await pyScript.run();
    return output;
  }
  
  // Example usage:
  
  const output = runPythonScript('./client.py');
  console.log(output);
}