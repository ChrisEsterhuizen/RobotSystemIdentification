plot(PcontrolInput)
plot(PcontrolOutput)

% x=squeeze(PcontrolInput);
% y=squeeze(PcontrolOutput);
plot(PcontrolInput.Data,PcontrolOutput.Data)
[PcontrolInput,PcontrolOutput] = synchronize(PcontrolInput,PcontrolInput,'Union'); plot(PcontrolInput.Data,PcontrolOutput.Data)