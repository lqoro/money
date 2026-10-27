FROM python:3.13-slim
WORKDIR /app
# Node + the Claude Code CLI: the brain runs on your Claude plan through `claude -p`.
RUN apt-get update && apt-get install -y --no-install-recommends nodejs npm ca-certificates \
    && npm install -g @anthropic-ai/claude-code \
    && apt-get purge -y npm && apt-get autoremove -y && rm -rf /var/lib/apt/lists/* /root/.npm
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY agent ./agent
COPY knowledge ./knowledge
COPY SOUL.md .
ENV PYTHONUNBUFFERED=1
VOLUME ["/app/memory"]
CMD ["python", "-m", "agent", "run"]
