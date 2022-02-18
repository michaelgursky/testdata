import 'https://deno.land/x/flat@0.0.14/mod.ts'

// install requirements with pip
const pip_install = Deno.run({
    cmd: ['python', '-m', 'pip', 'install', '-r', 'requirements.txt'],
});

await pip_install.status();

// Forwards the execution to the python script
const py_run = Deno.run({
    cmd: ['python', './weather-xml.py'].concat(Deno.args),
});

await py_run.status();
