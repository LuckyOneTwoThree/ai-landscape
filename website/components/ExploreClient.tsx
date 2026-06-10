'use client';

import React, { useState, useMemo } from 'react';
import { Tool } from '../lib/yaml';
import ToolCard from './ToolCard';
import styles from '../app/explore/page.module.css';
import { ChevronLeft } from 'lucide-react';
import Link from 'next/link';

interface ExploreClientProps {
  initialTools: Tool[];
  categories: string[];
  locale?: string;
}

const CATEGORY_MAP: Record<string, string> = {
  'applications/coding-ide': '应用 / 编程 IDE',
  'applications/search-research': '应用 / 搜索与研究',
  'applications/productivity': '应用 / 生产力',
  'applications/agent-tools': '应用 / 智能体工具',
  'data-and-knowledge/data-parsing': '数据与知识 / 数据解析',
  'data-and-knowledge/knowledge-graph': '数据与知识 / 知识图谱',
  'data-and-knowledge/synthetic-data': '数据与知识 / 合成数据',
  'data-and-knowledge/rag': '数据与知识 / RAG',
  'dev-frameworks/llm-framework': '开发框架 / LLM',
  'dev-frameworks/multi-agent': '开发框架 / 多智能体',
  'infrastructure/inference': '基础设施 / 推理引擎',
  'infrastructure/api-gateway': '基础设施 / API 网关',
  'infrastructure/vector-db': '基础设施 / 向量数据库',
  'infrastructure/gpu-cloud': '基础设施 / GPU 算力',
  'lowcode-platforms/ai-builder': '低代码 / AI 构建',
  'lowcode-platforms/workflow-automation': '低代码 / 工作流',
  'foundation-models/llm': '基础模型 / LLM',
  'foundation-models/multimodal': '基础模型 / 多模态',
  'foundation-models/embedding-reranker': '基础模型 / 词向量与重排',
  'observability/tracing': '可观测性 / 链路追踪',
  'observability/cost-monitoring': '可观测性 / 成本监控',
  'observability/benchmarks': '可观测性 / 评测基准',
  'safety-and-compliance/guardrails': '安全合规 / 护栏',
  'safety-and-compliance/content-moderation': '安全合规 / 内容审核',
  'safety-and-compliance/red-teaming': '安全合规 / 红蓝对抗',
  'safety-and-compliance/evaluation': '安全合规 / 评估',
  'skills-and-plugins/open-skills': '技能插件 / 开放技能',
  'skills-and-plugins/platform-plugins': '技能插件 / 平台插件',
  'tools-and-protocols/function-calling': '协议工具 / 函数调用',
  'tools-and-protocols/mcp': '协议工具 / MCP',
  'tools-and-protocols/browser-control': '协议工具 / 浏览器控制'
};

function formatCategory(cat: string) {
  return CATEGORY_MAP[cat] || cat;
}

export default function ExploreClient({ initialTools, categories, locale = 'zh' }: ExploreClientProps) {
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('');
  const [sortBy, setSortBy] = useState('stars-desc');

  const filteredAndSortedTools = useMemo(() => {
    let result = [...initialTools];

    // Filter by search query
    if (searchQuery) {
      const lowerQuery = searchQuery.toLowerCase();
      result = result.filter(
        tool => 
          String(tool.name).toLowerCase().includes(lowerQuery) || 
          (tool.description && String(tool.description).toLowerCase().includes(lowerQuery)) ||
          (tool.tags && Array.isArray(tool.tags) && tool.tags.some(t => String(t).toLowerCase().includes(lowerQuery)))
      );
    }

    // Filter by category
    if (selectedCategory) {
      result = result.filter(tool => tool.category === selectedCategory);
    }

    // Sort
    result.sort((a, b) => {
      if (sortBy === 'stars-desc') {
        return (b.stars || 0) - (a.stars || 0);
      } else if (sortBy === 'name-asc') {
        return a.name.localeCompare(b.name);
      }
      return 0;
    });

    return result;
  }, [initialTools, searchQuery, selectedCategory, sortBy]);

  const isEn = locale === 'en';

  return (
    <div className={styles.container}>
      <Link href={isEn ? "/en" : "/"} className={styles.backLink}>
        <ChevronLeft size={16} /> {isEn ? "Back to Home" : "返回首页"}
      </Link>

      <div className={styles.header}>
        <h1 className={styles.title}>{isEn ? "Explore AI Tools" : "探索 AI 工具库"}</h1>
        <p>{isEn ? "Discover and compare the most cutting-edge AI models, frameworks, and infrastructure." : "发现并比较最前沿的 AI 模型、框架与基础设施。"}</p>
      </div>

      <div className={styles.controls}>
        <input 
          type="text" 
          placeholder={isEn ? "Search tool name, description or tags..." : "搜索工具名称、描述或标签..."} 
          className={styles.search}
          value={searchQuery}
          onChange={e => setSearchQuery(e.target.value)}
        />
        
        <select 
          className={styles.select}
          value={selectedCategory}
          onChange={e => {
            setSelectedCategory(e.target.value);
            setSearchQuery('');
          }}
        >
          <option value="">{isEn ? "All Categories" : "所有分类"}</option>
          {categories.map(cat => (
            <option key={cat} value={cat}>{formatCategory(cat)}</option>
          ))}
        </select>

        <select 
          className={styles.select}
          value={sortBy}
          onChange={e => setSortBy(e.target.value)}
        >
          <option value="stars-desc">{isEn ? "Sort by Stars (High to Low)" : "按 Stars 排序 (高到低)"}</option>
          <option value="name-asc">{isEn ? "Sort by Name (A-Z)" : "按名称排序 (A-Z)"}</option>
        </select>
      </div>

      <div className={styles.grid}>
        {filteredAndSortedTools.map(tool => (
          <ToolCard key={tool.slug} tool={tool} locale={locale} />
        ))}
      </div>

      {filteredAndSortedTools.length === 0 && (
        <div className={styles.noResults}>
          <h3>{isEn ? "No matching tools found" : "未找到匹配的工具"}</h3>
          <p>{isEn ? "Please try changing the search query or filters" : "请尝试更改搜索词或过滤条件"}</p>
        </div>
      )}
    </div>
  );
}
