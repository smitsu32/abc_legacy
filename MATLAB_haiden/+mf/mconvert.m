function mconvert()
%MCONVERT この関数の概要をここに記述
%   詳細説明をここに記述
inputFile = input('Enter the input file name: ','s'); 
outputFile = input('Enter the output file name: ','s'); 

if ~isfile(inputFile)
    error('指定されたファイルが見つかりません。');
end

[filePath, ~, ~] = fileparts(which(inputFile));
cd(filePath);

if ~isfile(outputFile)
    fid = fopen(outputFile, 'wt'); % 書き込み用に新規ファイルを作成
    fprintf(fid, ''); % 空のファイルを作成
    fclose(fid);
    disp(['ファイル ', outputFile, ' を作成しました。']);
end

matlab.internal.liveeditor.openAndConvert(inputFile, outputFile);
fprintf('%sへの変換が完了しました\n',outputFile);
end

