"""
===================================
日志工具模块
功能：提供统一的日志记录功能
===================================
"""

import os
import logging
from pathlib import Path
from typing import Optional
from logging.handlers import RotatingFileHandler
from datetime import datetime


class Logger:
    """
    日志管理类
    提供统一的日志记录接口
    """
    
    # 类级别的日志器缓存
    _loggers = {}
    
    @classmethod
    def get_logger(
        cls,
        name: str = "MAD",
        log_file: Optional[str] = None,
        level: str = "INFO",
        log_format: Optional[str] = None,
        max_file_size: int = 10 * 1024 * 1024,  # 10MB
        backup_count: int = 5
    ) -> logging.Logger:
        """
        获取日志器实例（单例模式）
        
        Args:
            name: 日志器名称
            log_file: 日志文件路径
            level: 日志级别
            log_format: 日志格式
            max_file_size: 单个日志文件最大大小（字节）
            backup_count: 保留的日志文件备份数量
        
        Returns:
            logging.Logger: 日志器实例
        """
        # 如果已存在，直接返回
        if name in cls._loggers:
            return cls._loggers[name]
        
        # 创建新的日志器
        logger = logging.getLogger(name)
        logger.setLevel(getattr(logging, level.upper()))
        
        # 避免重复添加处理器
        if logger.handlers:
            return logger
        
        # 设置默认格式
        if log_format is None:
            log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        
        formatter = logging.Formatter(log_format)
        
        # 控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
        # 文件处理器（如果指定了日志文件）
        if log_file:
            # 确保日志目录存在
            log_path = Path(log_file)
            log_path.parent.mkdir(parents=True, exist_ok=True)
            
            # 使用RotatingFileHandler进行日志轮转
            file_handler = RotatingFileHandler(
                log_file,
                maxBytes=max_file_size,
                backupCount=backup_count,
                encoding='utf-8'
            )
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        
        # 缓存日志器
        cls._loggers[name] = logger
        
        return logger
    
    @classmethod
    def create_module_logger(cls, module_name: str) -> logging.Logger:
        """
        为特定模块创建日志器
        
        Args:
            module_name: 模块名称
        
        Returns:
            logging.Logger: 模块日志器
        """
        return cls.get_logger(f"MAD.{module_name}")


def setup_logging(config: dict) -> logging.Logger:
    """
    根据配置设置日志系统
    
    Args:
        config: 日志配置字典
    
    Returns:
        logging.Logger: 配置好的主日志器
    """
    log_config = config.get('logging', {})
    
    logger = Logger.get_logger(
        name="MAD",
        log_file=log_config.get('log_file', './logs/system.log'),
        level=log_config.get('level', 'INFO'),
        log_format=log_config.get('log_format'),
        max_file_size=log_config.get('max_file_size', 10485760),
        backup_count=log_config.get('backup_count', 5)
    )
    
    logger.info("=" * 60)
    logger.info("日志系统初始化完成")
    logger.info(f"日志级别: {log_config.get('level', 'INFO')}")
    logger.info(f"日志文件: {log_config.get('log_file', './logs/system.log')}")
    logger.info("=" * 60)
    
    return logger


class DebateLogger:
    """
    辩论过程专用日志记录器
    记录辩论的详细过程
    """
    
    def __init__(self, log_dir: str = "./logs/debates"):
        """
        初始化辩论日志器
        
        Args:
            log_dir: 辩论日志目录
        """
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)
        
        # 创建当前辩论的日志文件
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_file = self.log_dir / f"debate_{timestamp}.log"
        
        self.logger = Logger.get_logger(
            name=f"Debate_{timestamp}",
            log_file=str(self.log_file),
            level="DEBUG"
        )
    
    def log_debate_start(self, components: list, config: dict):
        """记录辩论开始"""
        self.logger.info("=" * 80)
        self.logger.info("辩论开始")
        self.logger.info("=" * 80)
        self.logger.info(f"化学组分: {', '.join(components)}")
        self.logger.info(f"最大轮数: {config.get('max_rounds', 10)}")
        self.logger.info(f"共识阈值: {config.get('consensus_threshold', 3)}")
        self.logger.info("")
    
    def log_round_start(self, round_num: int):
        """记录辩论轮次开始"""
        self.logger.info("-" * 80)
        self.logger.info(f"第 {round_num} 轮辩论开始")
        self.logger.info("-" * 80)
    
    def log_agent_response(
        self,
        agent_name: str,
        response: str,
        reaction_type: str = None,
        overpotential: float = None
    ):
        """记录Agent响应"""
        self.logger.info(f"\n[{agent_name}]")
        self.logger.info(f"响应: {response[:200]}..." if len(response) > 200 else f"响应: {response}")
        if reaction_type:
            self.logger.info(f"推荐反应: {reaction_type}")
        if overpotential:
            self.logger.info(f"过电势: {overpotential}")
    
    def log_consensus_check(self, consensus: bool, details: str):
        """记录共识检查结果"""
        status = "✓ 达成共识" if consensus else "✗ 未达成共识"
        self.logger.info(f"\n{status}")
        self.logger.info(f"详情: {details}")
    
    def log_debate_end(self, result: dict):
        """记录辩论结束"""
        self.logger.info("")
        self.logger.info("=" * 80)
        self.logger.info("辩论结束")
        self.logger.info("=" * 80)
        self.logger.info(f"最终结果: {result.get('final_reaction_type', '未确定')}")
        self.logger.info(f"过电势: {result.get('final_overpotential', '未估算')}")
        self.logger.info(f"辩论轮数: {result.get('debate_rounds', 0)}")
        self.logger.info(f"耗时: {result.get('time_elapsed', 0):.2f}秒")
        self.logger.info(f"共识达成: {'是' if result.get('consensus_reached') else '否'}")
        self.logger.info("=" * 80)
    
    def get_log_file_path(self) -> str:
        """获取日志文件路径"""
        return str(self.log_file)


# ===================================
# 使用示例
# ===================================
if __name__ == "__main__":
    # 基本用法
    logger = Logger.get_logger("TestModule")
    logger.debug("这是调试信息")
    logger.info("这是普通信息")
    logger.warning("这是警告信息")
    logger.error("这是错误信息")
    
    # 辩论日志器
    debate_logger = DebateLogger()
    debate_logger.log_debate_start(
        components=["A", "B", "C"],
        config={"max_rounds": 10, "consensus_threshold": 3}
    )
    debate_logger.log_agent_response(
        agent_name="Agent1",
        response="我认为应该选择反应类型A",
        reaction_type="氧化还原反应"
    )
    
    print(f"辩论日志保存在: {debate_logger.get_log_file_path()}")
