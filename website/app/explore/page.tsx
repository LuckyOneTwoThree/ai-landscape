import { getAllTools, getCategories } from '@/lib/yaml';
import ExploreClient from '@/components/ExploreClient';

export const metadata = {
  title: '探索 AI 工具 - AI Landscape',
  description: '全网最全的 AI 开发者生态工具库，包含大模型、开发框架、向量数据库等。',
};

export default function ExplorePage() {
  const tools = getAllTools();
  const categories = getCategories();

  return <ExploreClient initialTools={tools} categories={categories} />;
}
