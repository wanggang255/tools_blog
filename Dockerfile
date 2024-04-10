# 设置基础镜像
FROM python:3.9

# 设置工作目录
WORKDIR /app

# 复制应用程序代码到容器中
COPY . /app

# 安装应用程序依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露应用程序所使用的端口
EXPOSE 8000

# 启动应用程序
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]