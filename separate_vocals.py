from spleeter.separator import Separator

def main():
    # 初始化分离器（使用2stems模型：人声和伴奏）
    separator = Separator('spleeter:2stems')
    # 输入音频文件路径
    input_audio = "input.aac"
    # 输出目录
    output_dir = "output"
    # 执行分离
    separator.separate_to_file(input_audio, output_dir)
    print(f"分离完成！结果保存在 {output_dir}/")
    
if __name__ == "__main__":
    main()
