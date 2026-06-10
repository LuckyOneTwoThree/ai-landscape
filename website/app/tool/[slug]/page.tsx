import React from 'react';
import Link from 'next/link';
import { notFound } from 'next/navigation';
import { getAllTools, getToolBySlug } from '@/lib/yaml';
import { Star, ChevronLeft } from 'lucide-react';
import styles from './page.module.css';

// Generate static paths at build time
export function generateStaticParams() {
  const tools = getAllTools();
  return tools.map((tool) => ({
    slug: tool.slug,
  }));
}

// Generate dynamic metadata for SEO
export function generateMetadata({ params }: { params: { slug: string } }) {
  const tool = getToolBySlug(params.slug);
  
  if (!tool) {
    return {
      title: 'Tool Not Found - AI Landscape',
    };
  }

  return {
    title: `${tool.name} - AI Landscape`,
    description: tool.description || `关于 ${tool.name} 的详细介绍、特点及开源生态。`,
    keywords: [...(tool.tags || []), tool.name, 'AI', '工具', '开源'],
  };
}

import ToolView from '@/components/ToolView';

export default function ToolPage({ params }: { params: { slug: string } }) {
  const tool = getToolBySlug(params.slug);
  return <ToolView tool={tool} locale="zh" />;
}
