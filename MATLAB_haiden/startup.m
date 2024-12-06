% startup.m: MATLAB起動時に実行されるプログラム

% Get the current file path
currentFolder = fileparts(mfilename('fullpath'));

% Add the current folder to the MATLAB path
addpath(genpath(currentFolder));
clearvars currentFolder
% load('CREST126.mat');

fprintf('startup.m >> ワークスペースを初期化しました\n')