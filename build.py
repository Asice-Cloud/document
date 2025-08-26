import os
import glob
from pathlib import Path

def process_markdown_files():
    """
    遍历docs/0x-xx/目录下的所有.md文件，处理路径并合并文档
    """
    # 设置路径
    docs_pattern = "docs/0*/**/*.md"
    readme_path = "README.md"
    afterword_path = "docs/afterword.md"
    output_path = "edocument.md"
    
    # 存储所有处理后的内容
    merged_content = []
    
    # 读取README.md作为开头
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            readme_content = f.read()
            merged_content.append(readme_content)
            print(f"已添加 README.md")
    else:
        print("警告: README.md 文件不存在")
    
    # 获取所有匹配的markdown文件并排序
    md_files = glob.glob(docs_pattern, recursive=True)
    md_files.sort()  # 确保文件顺序一致
    
    print(f"找到 {len(md_files)} 个markdown文件")
    
    # 处理每个markdown文件
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 替换路径引用
            content = content.replace("../../assets", "assets")
            
            # 添加文件分隔符
            merged_content.append(f"\n\n---\n\n# {os.path.basename(md_file)}\n\n")
            merged_content.append(content)
            
            print(f"已处理: {md_file}")
            
        except UnicodeDecodeError as e:
            print(f"Unicode解码错误 {md_file}: {e}")
            # 尝试使用不同的编码
            try:
                with open(md_file, 'r', encoding='gbk') as f:
                    content = f.read()
                content = content.replace("../../assets", "assets")
                merged_content.append(f"\n\n---\n\n# {os.path.basename(md_file)}\n\n")
                merged_content.append(content)
                print(f"已处理 (GBK编码): {md_file}")
            except Exception as e2:
                print(f"无法处理文件 {md_file}: {e2}")
        except Exception as e:
            print(f"处理文件错误 {md_file}: {e}")
    
    # 添加afterword.md
    if os.path.exists(afterword_path):
        try:
            with open(afterword_path, 'r', encoding='utf-8') as f:
                afterword_content = f.read()
            
            afterword_content = afterword_content.replace("../assets", "assets")
            
            merged_content.append("\n\n---\n\n# 后记\n\n")
            merged_content.append(afterword_content)
            print(f"已添加 afterword.md")
        except Exception as e:
            print(f"处理afterword.md错误: {e}")
    else:
        print("警告: docs/afterword.md 文件不存在")
    
    # 写入合并后的文件
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(''.join(merged_content))
        print(f"\n合并完成! 输出文件: {output_path}")
        return output_path
    except Exception as e:
        print(f"写入输出文件错误: {e}")
        return None

def generate_pdf_with_pandoc(markdown_file):
    """
    使用pandoc生成PDF，处理Unicode问题
    """
    if not os.path.exists(markdown_file):
        print(f"文件不存在: {markdown_file}")
        return False
    
    output_pdf = markdown_file.replace('.md', '.pdf')
    
    # pandoc命令，使用默认模板
    cmd = f'''pandoc "{markdown_file}" -o "{output_pdf}" --pdf-engine=xelatex --listings --toc --number-sections -V CJKmainfont="SimSun" -V geometry:margin=2cm'''
    
    print(f"执行命令: {cmd}")
    
    try:
        import subprocess
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding='utf-8')
        
        if result.returncode == 0:
            print(f"PDF生成成功: {output_pdf}")
            return True
        else:
            print(f"PDF生成失败:")
            print(f"错误信息: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"执行pandoc命令错误: {e}")
        return False

if __name__ == "__main__":
    # 处理并合并markdown文件
    output_file = process_markdown_files()
    
    print("\n脚本执行完成!")