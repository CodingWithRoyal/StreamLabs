const OBSWebSocket = require('obs-websocket-js').default;
const {EventSubscription} = require('obs-websocket-js')

const obs = new OBSWebSocket();

const connect = async() => {

  try {
    const {
      obsWebSocketVersion,
      negotiatedRpcVersion
    } = await obs.connect('ws://localhost:4455', 'rootroot', {
      eventSubscriptions: EventSubscription.All | EventSubscription.InputVolumeMeters,
      rpcVersion: 1
    });
    console.log(`Connected to server ${obsWebSocketVersion} (using RPC ${negotiatedRpcVersion})`)

    obs.on('CurrentProgramSceneChanged', (event) => {
      console.log('Current scene changed to', event.sceneName)
    });

    obs.on('InputVolumeMeters', (data) => {
      data.inputs.forEach(e => {
        if (e.inputName !== undefined && e.inputName === 'Mic/Aux') {
          const left = e.inputLevelsMul[0].reduce((a, b) => a + b)
          const right = e.inputLevelsMul[0].reduce((a, b) => a + b)

          console.log(`left: ${left} \t right: ${right}`)
        }
      });
    })
  } catch (error) {
    console.error('Failed to connect', error.code, error.message);
  } 

}

connect().then(r=>console.log)